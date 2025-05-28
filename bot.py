# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from web3 import Web3
import datetime, json
import config

# Web3 初始化
w3 = Web3(Web3.HTTPProvider(config.WEB3_PROVIDER_URI))
with open(config.CONTRACT_ABI_PATH) as f:
    abi = json.load(f)

contract = w3.eth.contract(address=Web3.to_checksum_address(config.CONTRACT_ADDRESS), abi=abi)
user_wallets = {}

async def bind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        eth_address = context.args[0]
        try:
            user_wallets[update.effective_user.id] = Web3.to_checksum_address(eth_address)
            await update.message.reply_text("✅ 钱包地址绑定成功")
        except:
            await update.message.reply_text("❌ 无效地址")
    else:
        await update.message.reply_text("用法：/bind 0xYourAddress")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if uid not in user_wallets:
        await update.message.reply_text("请先绑定钱包地址：/bind 0xYourAddress")
        return
    addr = user_wallets[uid]
    expiry = contract.functions.getExpiry(addr).call()
    active = contract.functions.isActive(addr).call()
    expiry_time = datetime.datetime.utcfromtimestamp(expiry).strftime('%Y-%m-%d %H:%M:%S')
    msg = f"{'✅ 订阅有效' if active else '❌ 订阅过期'}\n到期时间：{expiry_time} UTC"
    await update.message.reply_text(msg)

app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("bind", bind))
app.add_handler(CommandHandler("status", status))
app.run_polling()

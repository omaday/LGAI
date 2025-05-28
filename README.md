# LGAI Telegram Subscription Bot


项目介绍

    全球首款基于大数据AI行情预测机器人，目前已经稳定运行4年以上，社区数百人实战验证，胜率82%以上。采用会员订阅，目前项目已经实现盈利。和非小号，HTX，LOOPSPACE，多个KOL及社区合作，提供AI推送信号，直接间接覆盖WEB3百万用户。
通过AVAX公链实现会员订阅测试功能。
## 功能

- 用户通过绑定钱包地址进行订阅查询
- 查询是否已订阅 / 到期时间
- 
## 项目结构
telegram-subscription-bot/
├── bot.py                  # Telegram Bot 主程序
├── contract/
│   ├── SubscriptionService.sol  # 智能合约
│   └── deploy.js               # 部署脚本
├── abi.json               # 合约 ABI（由 Hardhat 编译得到）
├── config.py              # 配置文件
├── requirements.txt       # Python 依赖
└── README.md              # 使用说明


## 使用步骤

1. 安装依赖
  
  ```bash
  pip install -r requirements.txt
  配置 config.py：
  ```
  

Telegram Token

Web3 节点地址

合约地址

启动 Bot

**python bot.py**

bash
复制
编辑
python bot.py

用户使用指令：

/bind 0xYourAddress

/status

# 项目介绍

-全球首款基于大数据AI的WEB3行情预测机器人，胜率高达82%以上，已稳定运行4年。

![1748600835202](https://github.com/user-attachments/assets/09954f0f-60c1-4b74-8931-93c6e9a94a27)





# 在本地部署一条 Avalanche Subnet 公链，基于电报BOT完成用户订阅服务。
---

## 📦 所需工具

- Node.js（建议 v18+）

- Avalanche-CLI

- Docker（可选，用于子网节点隔离）

---

## 🧰 安装 Avalanche-CLI

```bash
curl -sSfL https://raw.githubusercontent.com/ava-labs/avalanche-cli/main/scripts/install.sh | sh -s
export PATH=~/bin:$PATH
```

验证安装：

```bash
avalanche --version
```

---

## ⚙️ 创建 Subnet 配置

```bash
avalanche subnet create mySubnet
```

按提示填写：

| 选项       | 建议值               |
| -------- | ----------------- |
| VM 类型    | SubnetEVM         |
| Chain ID | 12345（可自定义）       |
| 原生代币符号   | TET               |
| Gas 费设定  | 1.5 mil gas/s（默认） |
| 预编译      | 否                 |



---

## 🚀 本地部署 Subnet

```bash
avalanche subnet deploy mySubnet --local
```

CLI 会启动多个节点，并显示 RPC 端口信息，例如：

```
Local network node endpoints:
node2: http://127.0.0.1:9652/ext/bc/<chainID>/rpc
node3: http://127.0.0.1:9654/ext/bc/<chainID>/rpc
```

---

## 🖥️ 配置 MetaMask

添加网络：

- 网络名称：MySubnet Local

- RPC URL：http://127.0.0.1:9652/ext/bc//rpc

- Chain ID：12345

- 代币符号：TET

示意图：

![metamask subnet](https://docs.avax.network/_images/metamask_subnet.png)

---

## 🔧 Subnet 配置文件结构（位于 ~/.avalanche-cli/configs/subnets/mySubnet/）

```json
{
  "vm": "subnet-evm",
  "name": "mySubnet",
  "tokenName": "TET",
  "subnetEVMGenesis": {
    "config": {
      "chainId": 12345,
      "homesteadBlock": 0,
      "eip150Block": 0,
      "eip155Block": 0,
      "eip158Block": 0,
      "byzantiumBlock": 0
    },
    "alloc": {},
    "nonce": "0x0",
    "difficulty": "0x1",
    "gasLimit": "0x7A1200"
  }
}
```

如需预部署账号或代币分配，可编辑 `alloc`：

```json
"alloc": {
  "0xYourAddress": {
    "balance": "0xDE0B6B3A7640000"
  }
}
```

---

## 🧹 清理网络（重置）

```bash
avalanche network clean
```

---

## 🧪 可选：部署合约进行测试

使用 Remix IDE 或 Hardhat 连接 RPC http://127.0.0.1:9652/ext/bc/xxx/rpc 进行合约部署和测试。

---

## 📬 下一步：连接 Telegram Bot

- 连接合约地址、用户地址与 Bot 的 chatId

- 查询订阅有效期（从合约读取）

- 实现订阅状态推送或定期续费提示





###############################################分割线#####################################################################################################

以下是在 **本地 Avalanche C-Chain 网络（Local AVAX L1）** 上为用户部署和发送 NFT VIP 卡 的 **完整详细步骤**，涵盖部署合约、mint NFT 发送给用户，以及用户接收展示。

---

## 🧰 工具准备

- Node.js 环境
  
- Hardhat 开发框架（推荐）
  
- Avalanche 本地网络已启动（`localhost:9650`）
  
- 钱包（建议使用 MetaMask）
  

---

## 🧱 第一步：部署本地 Avalanche C-Chain 网络（已完成可跳过）

你应该已经运行了 AvalancheGo 节点，并开启了 C-Chain RPC：

bash

复制编辑

`http://127.0.0.1:9650/ext/bc/C/rpc`

---

## 🧱 第二步：初始化项目 + 安装依赖

bash

复制编辑

`mkdir avax-nft-local && cd avax-nft-local npm init -y npm install --save-dev hardhat npx hardhat`

选择 `Create a basic sample project`，然后安装依赖：

bash

复制编辑

`npm install @nomiclabs/hardhat-ethers ethers npm install @openzeppelin/contracts`

---

## 🧾 第三步：编写 ERC-721 合约

在 `contracts/MyNFT.sol``contracts/MyNFT.sol` 中创建合约文件：

---

## ⚙️ 第四步：配置 Hardhat 网络

修改 `hardhat.config.js`：

> 💡 私钥可以是 Avalanche 本地网络中创建的钱包账号（例如通过 Avalanche Wallet 创建的测试账户）。

---

## 🚀 第五步：部署合约

创建 `scripts/deploy.js`：

运行部署命令：

bash

复制编辑

`npx hardhat run scripts/deploy.js --network localavax`

---

## 🎁 第六步：为用户发送 NFT

创建 `scripts/mint.js`：

执行 mint 脚本：

bash

复制编辑

`npx hardhat run scripts/mint.js --network localavax`

---

## 👤 第七步：用户接收 NFT（展示）

用户可以使用 MetaMask 添加本地网络：

- **网络名称**：Local AVAX
  
- **RPC URL**：`http://127.0.0.1:9650/ext/bc/C/rpc`
  
- **链ID**：XXXXX
  
- **币种符号**：TEST
  

然后通过 MetaMask 查看钱包中是否收到 NFT。






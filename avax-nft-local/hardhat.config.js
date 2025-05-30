require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: "0.8.20",
  networks: {
    localavax: {
      url: "http://127.0.0.1:9650/ext/bc/C/rpc",
      chainId: 43112,
      accounts: ["0x私钥（无0x前缀）"]
    }
  }
};
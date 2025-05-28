const hre = require("hardhat");

async function main() {
    const TEST_TOKEN = "0x";
    const Sub = await hre.ethers.getContractFactory("SubscriptionService");
    const sub = await Sub.deploy(TET_TOKEN);
    await sub.waitForDeployment();
    console.log("Deployed to:", await sub.getAddress());
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});

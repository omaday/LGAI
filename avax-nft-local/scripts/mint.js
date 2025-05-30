async function main() {
  const [deployer] = await ethers.getSigners();

  const nftAddress = "0xNFT合约地址";
  const nft = await ethers.getContractAt("MyNFT", nftAddress);

  const recipient = "0x用户钱包地址";
  const metadataURI = "http://localhost:8080/1.json";

  const tx = await nft.safeMint(recipient, metadataURI);
  await tx.wait();
  console.log(`NFT minted to ${recipient}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
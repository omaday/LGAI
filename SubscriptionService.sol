// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
}

contract SubscriptionService {
    IERC20 public tetToken;

    struct Subscription {
        uint256 expiry;
    }

    mapping(address => Subscription) public subscriptions;

    uint256 public constant MONTHLY = 888 * 1e18;
    uint256 public constant QUARTERLY = 8888 * 1e18;
    uint256 public constant YEARLY = 88888 * 1e18;

    constructor(address _tetToken) {
        tetToken = IERC20(_tetToken);
    }

    function subscribe(uint8 planType) external {
        uint256 amount;
        uint256 duration;

        if (planType == 1) {
            amount = MONTHLY;
            duration = 30 days;
        } else if (planType == 3) {
            amount = QUARTERLY;
            duration = 90 days;
        } else if (planType == 12) {
            amount = YEARLY;
            duration = 365 days;
        } else {
            revert("Invalid plan");
        }

        require(tetToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        if (block.timestamp > subscriptions[msg.sender].expiry) {
            subscriptions[msg.sender].expiry = block.timestamp + duration;
        } else {
            subscriptions[msg.sender].expiry += duration;
        }
    }

    function getExpiry(address user) external view returns (uint256) {
        return subscriptions[user].expiry;
    }

    function isActive(address user) external view returns (bool) {
        return subscriptions[user].expiry > block.timestamp;
    }
}

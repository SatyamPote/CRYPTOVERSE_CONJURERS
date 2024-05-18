// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContentManagement {
    struct Content {
        uint256 id;
        address author;
        string ipfsHash;
        uint256 timestamp;
        uint256 upvotes;
        uint256 downvotes;
    }

    uint256 public nextContentId;
    mapping(uint256 => Content) public contents;

    event ContentCreated(uint256 id, address author, string ipfsHash, uint256 timestamp);
    event ContentUpvoted(uint256 id, address voter);
    event ContentDownvoted(uint256 id, address voter);

    function createContent(string memory ipfsHash) public {
        contents[nextContentId] = Content(nextContentId, msg.sender, ipfsHash, block.timestamp, 0, 0);
        emit ContentCreated(nextContentId, msg.sender, ipfsHash, block.timestamp);
        nextContentId++;
    }

    function upvoteContent(uint256 id) public {
        require(contents[id].author != address(0), "Content does not exist");
        contents[id].upvotes++;
        emit ContentUpvoted(id, msg.sender);
    }

    function downvoteContent(uint256 id) public {
        require(contents[id].author != address(0), "Content does not exist");
        contents[id].downvotes++;
        emit ContentDownvoted(id, msg.sender);
    }
}
const ContentManagement = artifacts.require("ContentManagement");

module.exports = function (deployer) {
    deployer.deploy(ContentManagement);
};
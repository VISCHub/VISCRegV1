// Please visit http://go.microsoft.com/fwlink/?LinkID=761099&clcid=0x409 for more information on settting up Github Webhooks

keccak256 = require('js-sha3').keccak256;
shajs = require('sha.js');

function sha256(txt) {
    return (new shajs.sha256().update(txt).digest('hex'));
}

module.exports = function (context, data) {
    // VISCBotToken
    context.log('VISCBotToken:', process.env.VISCBotToken);
    context.log('keccak256(vietlq)', keccak256('vietlq'));
    context.log('sha256(vietlq)', sha256('vietlq'));
    context.log('The full data is:', data);
    context.done();
};

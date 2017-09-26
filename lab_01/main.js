'use strict';

let fs = require('fs');

let fd = fs.openSync('./file', 'a+');
let fileStats = fs.fstatSync(fd);
let dataBuffer = new Buffer(fileStats.size);
let alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

fs.readSync(fd, dataBuffer, 0, fileStats.size, 0);

let dataString = dataBuffer.toString('utf8');
let dataArray = dataString.split('');

encrypt(dataArray, 'awd', 5, alphabet);

function encrypt(dataArray, keyWord, k, alphabet) {
    let alphabetBack = [];
    let cryptMap = {};

    for(let i = alphabet.length - 1; i >= 0; i--) {
        alphabetBack[i] = alphabet[i];
    }

    let keyWordArray = keyWord.split('');

    // Delete from alphabet all chars that already contained in keyWord
    for (let i = alphabet.length - 1; i >= 0; i--) {
        for (let j = keyWordArray.length - 1; j >= 0; j--) {
            if(keyWordArray[j] === alphabet[i]) {
                alphabet.splice(i, 1);
                break;
            }
        }
    }

    let movedChars = keyWordArray.concat(alphabet);
    shiftArrayToRight(movedChars, k);

    for(let i = alphabet.length - 1; i >= 0; i--) {
        cryptMap[alphabetBack[i]] = movedChars[i];
    }

    console.log(cryptMap);
}

function decrypt(dataArray, keyWord, k, alphabet) {
}

fs.closeSync(fd);

/* UTILS */

function shiftArrayToRight(arr, places) {
    for (var i = 0; i < places; i++) {
        arr.unshift(arr.pop());
    }
}
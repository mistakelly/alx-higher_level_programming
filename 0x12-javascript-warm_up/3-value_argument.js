#!/usr/bin/node
if (process.argv[2] === undefined)
{
    console.log('No argument');
}else{
    firstArg = process.argv.slice(2)
    console.log(firstArg)
}

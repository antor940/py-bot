// require the discord.js module
const Discord = require('discord.js');

// create a new Discord client
const client = new Discord.Client();

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
	console.log('Ready!');
});

// login to Discord with your app's token
client.login('ODA2NDU3NTk1MjYxODc4Mjky.YBpuKQ.oJ7o3aDDezmYZwwQU1PrRq5LNB4');
const discord = require('discord.js');
const Client = new Discord.Client();
//CLIENT EVENTS
client.on("ready", () => {
  console.log("Ready to boom your ears | Bot created by ANTOR");
  client.user.setActivity("Sourced By ANNTOR#8129");
});
 
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
 
client.on('message', msg => {
  if (msg.content === 'Hi') {
    msg.reply('Hi');
  }
});
client.on('message', msg => {
  if (msg.content === 'hi') {
    msg.reply('hi');
  }
});
client.on('message', msg => {
  if (msg.content === 'HI') {
    msg.reply('HI');
  }
});
client.on('message', msg => {
  if (msg.content === 'hello') {
    msg.reply('hello');
  }
});
client.on('message', msg => {
  if (msg.content === 'Hello') {
    msg.reply('Hello');
  }
});
client.on('message', msg => {
  if (msg.content === 'HELLO') {
    msg.reply('HELLO');
  }
});
client.on('message', msg => {
  if (msg.content === 'bye') {
    msg.reply('bye🙋');
  }
});
client.on('message', msg => {
  if (msg.content === 'Bye') {
    msg.reply('Bye🙋');
  }
});
client.on('message', msg => {
  if (msg.content === 'BYE') {
    msg.reply('BYE🙋');
  }
});
client.on('message', msg => {
  if (msg.content === 'Bye🙋') {
    msg.reply('Bye🙋');
  }
});
client.on('message', msg => {
  if (msg.content === 'bye🙋') {
    msg.reply('bye🙋');
  }
});
client.on('message', msg => {
  if (msg.content === 'BYE🙋') {
    msg.reply('BYE🙋');
  }
});
client.on('message', msg => {
  if (msg.content === 'good night') {
    msg.reply('good night😴');
  }
});
client.on('message', msg => {
  if (msg.content === 'Good night') {
    msg.reply('Good night😴');
  }
});
client.on('message', msg => {
  if (msg.content === 'GOOD NIGHT') {
    msg.reply('GOOD NIGHT😴');
  }
});
client.on('message', msg => {
  if (msg.content === 'GOOD MORNING') {
    msg.reply('GOOD MORNING🥱');
  }
});
client.on('message', msg => {
  if (msg.content === 'good morning') {
    msg.reply('good morning🥱');
  }
});
client.on('message', msg => {
  if (msg.content === 'Good morning') {
    msg.reply('Good morning🥱');
  }
});
client.on('message', msg => {
  if (msg.content === 'ee') {
    msg.reply(':a: ')
  }
});

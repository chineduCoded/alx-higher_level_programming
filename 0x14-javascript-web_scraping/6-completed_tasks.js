#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((task) => {
      if (task.completed) {
        const userId = task.userId;
        completedTasks[userId] = completedTasks[userId] ? completedTasks[userId] + 1 : 1;
      }
    });

    console.log(completedTasks);
  }
});

var fs = require('fs');

fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
    if (err) throw err;
    console.log('Saved!');
  });

// let btn = document.getElementsByClassName("cf")[0]

// btn.addEventListener("click", function (e) {
//     let text = document.getElementsByClassName("filename")[0].value
//     console.log(text);
// })
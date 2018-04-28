const express = require('express');
const path = require('path');
const port = process.env.PORT || 8000;
const app = express();
let count = 0;

app.use(express.static(path.join(__dirname, 'client')));

const server = app.listen(port, () => console.log(`Listening on port ${ port }`));
const io = require('socket.io')(server);

io.on('connection', socket => {
    console.log('Socket connected');
//changed per the lecture so count goes up before the send//
    socket.on('updateClicked', function() {
        io.emit('update', ++count);
    });

    socket.on('resetCount', function() {
        count = 0;
        io.emit('update', count);
    });
//this sends the current count to a new user
    socket.emit('update', count);
});

//--Can also set a function outside the socket calls: from lecture
//function updateNumber(number) {
 //   io.emit('update', number);
//}
// on the socket.on calls just send updateNumber(++count or count = 0)
//to this function

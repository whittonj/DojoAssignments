const users = [];
const messages = [];
//from solution - to see create user list
function isUser(user) {
  const userCount = users.length;

  for (var i = 0; i < userCount; i++) {
    if (user == users[i]) {
      return true;
    }
  }
  return false;
}

module.exports = function Route(app, server) {
  const io = require("socket.io").listen(server);
//exisiting user is not working... not sure what I broke
  io.sockets.on("connection", function(socket) {
    socket.on("page_load", function(data) {
      const existingUser = isUser(data.user);
      const event = existingUser ? 'existing_user' : 'load_messages';
      data = existingUser ? {
                    error: "This user already exits"
                  } : { current_user: data.user, messages: messages };

      if (!existingUser) {
        users.push(data.user);
      }

      socket.emit(event, data);
    });

    socket.on("new_message", function(data) {
      messages.push({ name: data.user, message: data.message });
      io.emit("post_new_message", { new_message: data.message, user: data.user });
    });
  });

  app.get("/", function(request, response){
    response.render("index")
  });
};

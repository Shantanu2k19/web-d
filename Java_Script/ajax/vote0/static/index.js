document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket, standard syntax
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => 
    {
        // Each button should emit a "submit vote" event
        document.querySelectorAll('button').forEach(button =>  
        {  //select all buttons
            button.onclick = () => 
            {
                const selection = button.dataset.vote;
                socket.emit('submit vote', {'selection': selection});
            //emiting event named : submit vote, passing the data assosiated(json object, {name,value})
            };
        });
    });

    // When a new vote is announced, add to the unordered list
    socket.on('announce vote', data => {
        const li = document.createElement('li'); //create list item
        li.innerHTML = `Vote recorded: ${data.selection}`;
        document.querySelector('#votes').append(li);
    });
});

document.addEventListener('DOMContentLoaded', function()
            			{document.querySelector('button').onclick = count;}  );


let counter = 0;

function count(){
    counter++;
    document.querySelector('#counter').innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`Counter is at ${counter}!`);
    }
}

/*
html event : anything that is done on/by the browser, like moving cursor

DOM : document object model, 
DOMContentLoaded: when all the html inside our page is loaded by the browser
meaning, when the content of dom is loaded, run function()  #line 1
function definition is given in the argument itself

line 2: extract the button from the page(queryselector), set onclick attribute to function count #here count function used as a value 
*/

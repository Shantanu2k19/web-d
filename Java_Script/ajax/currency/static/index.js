document.addEventListener('DOMContentLoaded', () => 
{

    document.querySelector('#form').onsubmit = () => 
    {

        //creating a new onject that will allow to make a  ajax request to some web server to get information 
        const request = new XMLHttpRequest();

        //get the user typed currency
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert'); //new request, request this to url /convert

        // Callback function for when request completes
        request.onload = () => 
        {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            //data variable have whatever came back from /convert route
            // Update the result div, if data successfully received
            if (data.success) 
            {
                const contents = `1 USD is equal to ${data.rate} ${currency}.`
                document.querySelector('#result').innerHTML = contents;
            }
            else 
            {
                document.querySelector('#result').innerHTML = 'There was an error.';
            }
        }

        // Add data to send with request
        const data = new FormData();
        data.append('currency', currency);

        // Send request
        request.send(data);//data about currency to /convert route
        return false;//to stop page from reloading
    };

});

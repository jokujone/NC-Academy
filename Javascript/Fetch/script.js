async function getData() {

    const loss = document.getElementById("loss");
    const button = document.getElementById("button");

    const url = "https://jsonplaceholder.typicode.com/users";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
        
        result.forEach(element => {
            var p = document.createElement("p");
            var string = document.createTextNode(element.name);
            p.appendChild(string)
            document.body.appendChild(p);
            console.log(element.name)

        });
        var losstext = document.createTextNode("In memory of...")
        loss.appendChild(losstext)
        button.style.visibility = "hidden"
    } catch (error) {
        console.error(error.message);
    }
}
async function getattractions() {
    let myObject = await fetch("/");
    let myattractions = await myObject.json();
    console.log(myattractions)
}

// async function place_order() {
//     const response = await fetch("api/placeorder", {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify(shoppingCart)
//     })
//     console.log(response.statusText)
// }


// export async function get_fruit() {
//     const response = await fetch("mancala/api/start", {
//         method: "POST",
//         headers: {
//             Accept: "application/json",
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//             player1: player1,
//             player2: player2,
//         }),
//     });
//
//     if (response.ok) {
//         const gameState = await response.json();
//         return gameState as GameState;
//     } else {
//         return {
//             statusCode: response.status,
//             statusText: response.statusText
//         };
//     }
// }
async function fetchData() {
  try {
    const response = await fetch("http://127.0.0.1:8000/books");
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  fetchData();
  // Step 1: Create the parent div element
  const parentDiv = document.createElement("div");
  parentDiv.className = "book_container";

  // Step 2: Create the first child div element
  const childDiv = document.createElement("div");
  childDiv.className = "book_img";

  // Step 3: Create the image element
  const childphoto = document.createElement("img");
  childphoto.src = "";
  childphoto.style =
    "max-width: 100%; max-height: 100%; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);";

  // Step 4: Create the second child div element
  const childDiv1 = document.createElement("div");
  childDiv1.className = "book_title";

  // Step 5: Append the image and second child div to the first child div
  childDiv.appendChild(childphoto);
  childDiv.appendChild(childDiv1);

  // Step 6: Append the first child div to the parent div
  parentDiv.appendChild(childDiv);

  // Step 7: Append the parent div to the book shelf element in the DOM
  const bookShelf = document.getElementsByClassName("book_shelf");
  if (bookShelf.length > 0) {
    bookShelf[0].appendChild(parentDiv); // Select the first element from the collection
  } else {
    console.error('No elements found with class name "book_shelf"');
  }
});

function countWordsAndCharacters() {
    const text = document.getElementById('text').value;
    const wordCount = text.trim().split(/\s+/).length;
    const charCount = text.length;

    document.getElementById('wordCount').textContent = `Number of words: ${wordCount}`;
    document.getElementById('charCount').textContent = `Number of characters: ${charCount}`;
}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Word and Character Counter</title>
</head>
<body>
    <h1>Word and Character Counter</h1>
    <textarea id="text" rows="5" cols="30" placeholder="Type your text here..."></textarea>
    <button onclick="countWordsAndCharacters()">Count</button>
    <p id="wordCount">Number of words: 0</p>
    <p id="charCount">Number of characters: 0</p>
</body>
</html>
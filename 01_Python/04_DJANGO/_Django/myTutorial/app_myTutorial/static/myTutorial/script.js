// JavaScript to handle showing content when a menu is clicked
function showContent(page) {
    const contentDiv = document.getElementById("content");

    // Sample content for each section
    let content = '';
    switch (page) {
        case 'oracle':
            content = `<h2>Oracle Tutorial</h2><p>Welcome to the Oracle tutorial section!</p>`;
            break;
        case 'linux':
            content = `<h2>Linux Tutorial</h2><p>Welcome to the Linux tutorial section!</p>`;
            break;
        case 'postgresql':
            content = `<h2>PostgreSQL Tutorial</h2><p>Welcome to the PostgreSQL tutorial section!</p>`;
            break;
        case 'python':
            content = `<h2>Python Tutorial</h2><p>Welcome to the Python tutorial section!</p>`;
            break;
        case 'django':
            content = `<h2>Django Tutorial</h2><p>Welcome to the Django tutorial section!</p>`;
            break;
        case 'pyqt5':
            content = `<h2>PyQt5 Tutorial</h2><p>Welcome to the PyQt5 tutorial section!</p>`;
            break;
        case 'tkinter':
            content = `<h2>Tkinter Tutorial</h2><p>Welcome to the Tkinter tutorial section!</p>`;
            break;
        case 'github':
            content = `<h2>GitHub Tutorial</h2><p>Welcome to the GitHub tutorial section!</p>`;
            break;
        case 'personal':
            content = `<h2>Personal Page</h2><p>Welcome to your personal page!</p>`;
            break;
        default:
            content = `<h2>Welcome to My Tutorial</h2><p>Select a topic from the navbar to view a sample page.</p>`;
    }

    // Set the new content in the content div
    contentDiv.innerHTML = content;
}

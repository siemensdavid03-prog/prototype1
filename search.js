const urlParams = new URLSearchParams(window.location.search);
        const searchQuery = urlParams.get('search');
        if (searchQuery) {
            document.getElementById('search-title').innerText = "Search Results for " + searchQuery;
        } else {
            document.getElementById('search-title').innerText = "No Search Results";
        }

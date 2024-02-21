# DEVLOG
### TOC
    + Branch and current development
    + Issues by app
    + Frontend changes
    + Feature requests
    + Bugs




### Branch and current development
    The most recent branch featuring all currently unmerged updates to the main codebase live in `dev/v0.3.0`.

This branch's development goals are as follows:
    + Setting up a many-to-many relationship between user created content (images) and user interactions with that object.
    + Customize form-behavior to function smoothly with JS bookmarklet. Has custom save method that downloads image at url.
    + Implement minimal JavaScript with Django for various features
    + Build out the Bookmarklet with JS
    + Use `easy-thumbnails` to generate and render thumbnails properly
    + Implement asynchronous HTTP requests via JS


### Issues By APp

### Frontend changes

    + `account.dashboard`
        - Menu needs to be separated from tile div element, not rendering correctly
        - Title text on level-item elements needs to be white against dark bg
        - Get rid of primary colored parent element to user profile card
        - Consider putting all tile elements in parent container with colored background.


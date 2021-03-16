import React from 'react';

function Upload(){
    return(
        <form action="./data-cleaner-app/cleandata.py" method="POST" enctype="multipart/form-data">
            <input type="file" name="file"/>
            <input type="submit" value="Submit"/>
        </form>

    );
}

export default Upload;
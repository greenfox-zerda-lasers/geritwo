function deleteTask(id){
  let postList = new XMLHttpRequest();
  postList.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);

  postList.setRequestHeader("Content-type", "application/json");

  postList.send(null);
  postList.onreadystatechange = delReady;

  function delReady(rsp) {
    if (postList.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(postList.response))
    };
  };
};
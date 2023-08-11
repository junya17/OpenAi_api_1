function search() {
    // クエリの取得
    var query = document.getElementById('query').value;
  
    // POSTリクエストの送信
    fetch('/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt: query }),
    })
    .then(response => response.json())
    .then(data => {
      // 結果の表示
      document.getElementById('results').innerHTML = data.text;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  
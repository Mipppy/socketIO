class SocketIO {
    emit(message, data) {
        return new Promise((resolve, reject) => {
            fetch('/socket', {
                method: "POST",
                body: JSON.stringify({ type: message, data: { data } }),
                headers: { 'Content-Type': 'application/json;' }
            }).then(response => {
                if (!response.ok) {
                    reject( Error(`Network response was not ok. ${response}`))
                }
                return response.json()
            }).then(data => {
                resolve(data)
            }).catch(error => {
                reject(Error(`Fetch request failed: ${error}`))
            })
        })
    }
}
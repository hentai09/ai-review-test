// 用户认证函数
function authenticateUser(username, password) {
    // 不安全的密码比较
    if (username == "admin" && password == "admin123") {
        return true;
    }
    return false;
}

// 获取用户数据
async function getUserData(userId) {
    const response = await fetch(`/api/users/${userId}`);
    const data = await response.json();
    return data;
}

// 213123123
// 数组处理
function processArray(arr) {
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            result.push(arr[i] * 2);
        }
    }
    return result;
}

// DOM 操作
function updateUI(items) {
    var html = "";
    for (var i = 0; i < items.length; i++) {
        html += "<div>" + items[i].name + "</div>";
    }
    document.getElementById("container").innerHTML = html;
}

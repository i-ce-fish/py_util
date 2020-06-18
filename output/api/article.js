import request from "@/utils/request"


export function getArticles(params) {
    return request({
        url: "/api/articles",
        method: "get",
        params
    })
}

export function getArticle(id) {
    return request({
        url: `/api/articles/${id}`,
        method: "get"
    })
}

export function addArticle(data) {
    return request({
        url: "/api/articles",
        method: "post",
        data
    })
}

export function putArticle(id, data) {
    return request({
        url: `/api/articles/${id}`,
        method: "put",
        data
    })
}

export function delArticle(id) {
    return request({
        url: `/api/articles/${id}`,
        method: "delete"
    })
}
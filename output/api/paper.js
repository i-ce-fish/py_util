import request from "@/utils/request"


export function getPapers(params) {
    return request({
        url: "/api/papers",
        method: "get",
        params
    })
}

export function getPaper(id) {
    return request({
        url: `/api/papers/${id}`,
        method: "get"
    })
}

export function addPaper(data) {
    return request({
        url: "/api/papers",
        method: "post",
        data
    })
}

export function putPaper(id, data) {
    return request({
        url: `/api/papers/${id}`,
        method: "put",
        data
    })
}

export function delPaper(id) {
    return request({
        url: `/api/papers/${id}`,
        method: "delete"
    })
}
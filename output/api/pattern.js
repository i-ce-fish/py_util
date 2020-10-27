import request from "@/utils/request"


export function getPatterns(params) {
    return request({
        url: "/api/patterns",
        method: "get",
        params
    })
}

export function getPattern(id) {
    return request({
        url: `/api/patterns/${id}`,
        method: "get"
    })
}

export function addPattern(data) {
    return request({
        url: "/api/patterns",
        method: "post",
        data
    })
}

export function putPattern(id, data) {
    return request({
        url: `/api/patterns/${id}`,
        method: "put",
        data
    })
}

export function delPattern(id) {
    return request({
        url: `/api/patterns/${id}`,
        method: "delete"
    })
}
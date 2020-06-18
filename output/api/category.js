import request from "@/utils/request"


export function getCategories(params) {
    return request({
        url: "/api/categories",
        method: "get",
        params
    })
}

export function getCategory(id) {
    return request({
        url: `/api/categories/${id}`,
        method: "get"
    })
}

export function addCategory(data) {
    return request({
        url: "/api/categories",
        method: "post",
        data
    })
}

export function putCategory(id, data) {
    return request({
        url: `/api/categories/${id}`,
        method: "put",
        data
    })
}

export function delCategory(id) {
    return request({
        url: `/api/categories/${id}`,
        method: "delete"
    })
}
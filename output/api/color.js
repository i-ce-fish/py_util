import request from "@/utils/request"


export function getColors(params) {
    return request({
        url: "/api/colors",
        method: "get",
        params
    })
}

export function getColor(id) {
    return request({
        url: `/api/colors/${id}`,
        method: "get"
    })
}

export function addColor(data) {
    return request({
        url: "/api/colors",
        method: "post",
        data
    })
}

export function putColor(id, data) {
    return request({
        url: `/api/colors/${id}`,
        method: "put",
        data
    })
}

export function delColor(id) {
    return request({
        url: `/api/colors/${id}`,
        method: "delete"
    })
}
import request from "@/utils/request"


export function getColors(params) {
    return request({
        url: "/api/colors",
        method: "get",
        params
    })
}

export function getColor2(id) {
    return request({
        url: `/api/colors/${id}`,
        method: "get"
    })
}

export function addColor2(data) {
    return request({
        url: "/api/colors",
        method: "post",
        data
    })
}

export function putColor2(id, data) {
    return request({
        url: `/api/colors/${id}`,
        method: "put",
        data
    })
}

export function delColor2(id) {
    return request({
        url: `/api/colors/${id}`,
        method: "delete"
    })
}
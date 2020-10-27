import request from "@/utils/request"


export function getMaterials(params) {
    return request({
        url: "/api/materials",
        method: "get",
        params
    })
}

export function getMaterial(id) {
    return request({
        url: `/api/materials/${id}`,
        method: "get"
    })
}

export function addMaterial(data) {
    return request({
        url: "/api/materials",
        method: "post",
        data
    })
}

export function putMaterial(id, data) {
    return request({
        url: `/api/materials/${id}`,
        method: "put",
        data
    })
}

export function delMaterial(id) {
    return request({
        url: `/api/materials/${id}`,
        method: "delete"
    })
}
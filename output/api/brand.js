import request from "@/utils/request"


export function getBrands(params) {
    return request({
        url: "/api/brands",
        method: "get",
        params
    })
}

export function getBrand(id) {
    return request({
        url: `/api/brands/${id}`,
        method: "get"
    })
}

export function addBrand(data) {
    return request({
        url: "/api/brands",
        method: "post",
        data
    })
}

export function putBrand(id, data) {
    return request({
        url: `/api/brands/${id}`,
        method: "put",
        data
    })
}

export function delBrand(id) {
    return request({
        url: `/api/brands/${id}`,
        method: "delete"
    })
}
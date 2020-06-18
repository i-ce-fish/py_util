import request from "@/utils/request"


export function getCatalogs(params) {
    return request({
        url: "/api/catalogs",
        method: "get",
        params
    })
}

export function getCatalog(id) {
    return request({
        url: `/api/catalogs/${id}`,
        method: "get"
    })
}

export function addCatalog(data) {
    return request({
        url: "/api/catalogs",
        method: "post",
        data
    })
}

export function putCatalog(id, data) {
    return request({
        url: `/api/catalogs/${id}`,
        method: "put",
        data
    })
}

export function delCatalog(id) {
    return request({
        url: `/api/catalogs/${id}`,
        method: "delete"
    })
}
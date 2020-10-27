import request from "@/utils/request"


export function getGoodfabrics(params) {
    return request({
        url: "/api/goodfabrics",
        method: "get",
        params
    })
}

export function getGoodfabric(id) {
    return request({
        url: `/api/goodfabrics/${id}`,
        method: "get"
    })
}

export function addGoodfabric(data) {
    return request({
        url: "/api/goodfabrics",
        method: "post",
        data
    })
}

export function putGoodfabric(id, data) {
    return request({
        url: `/api/goodfabrics/${id}`,
        method: "put",
        data
    })
}

export function delGoodfabric(id) {
    return request({
        url: `/api/goodfabrics/${id}`,
        method: "delete"
    })
}
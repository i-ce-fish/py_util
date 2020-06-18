import request from "@/utils/request"


export function getGoodorders(params) {
    return request({
        url: "/api/goodorders",
        method: "get",
        params
    })
}

export function getGoodorder(id) {
    return request({
        url: `/api/goodorders/${id}`,
        method: "get"
    })
}

export function addGoodorder(data) {
    return request({
        url: "/api/goodorders",
        method: "post",
        data
    })
}

export function putGoodorder(id, data) {
    return request({
        url: `/api/goodorders/${id}`,
        method: "put",
        data
    })
}

export function delGoodorder(id) {
    return request({
        url: `/api/goodorders/${id}`,
        method: "delete"
    })
}
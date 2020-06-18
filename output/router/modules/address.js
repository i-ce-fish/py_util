import Layout from "@/layout"

const addressRouter = {
    path: "/address",
    name: "address",
    redirect: "/address/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/address/index"),
        meta: { title: "地址表管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/address/edit"),
        hidden: true,
        meta: { title: "修改地址表" }
    },
    {
        path: "add",
        component: () => import("@/views/address/add"),
        hidden: true,
        meta: { title: "添加地址表" }
    }
    ]
}

export default addressRouter
import Layout from "@/layout"

const goodorderRouter = {
    path: "/goodorder",
    name: "goodorder",
    redirect: "/goodorder/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/goodorder/index"),
        meta: { title: "订单表管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodorder/edit"),
        hidden: true,
        meta: { title: "修改订单表" }
    },
    {
        path: "add",
        component: () => import("@/views/goodorder/add"),
        hidden: true,
        meta: { title: "添加订单表" }
    }
    ]
}

export default goodorderRouter
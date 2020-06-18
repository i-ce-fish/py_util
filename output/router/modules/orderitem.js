import Layout from "@/layout"

const orderitemRouter = {
    path: "/orderitem",
    name: "orderitem",
    redirect: "/orderitem/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/orderitem/index"),
        meta: { title: "订单项目标管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/orderitem/edit"),
        hidden: true,
        meta: { title: "修改订单项目标" }
    },
    {
        path: "add",
        component: () => import("@/views/orderitem/add"),
        hidden: true,
        meta: { title: "添加订单项目标" }
    }
    ]
}

export default orderitemRouter
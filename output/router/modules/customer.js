import Layout from "@/layout"

const customerRouter = {
    path: "/customer",
    name: "customer",
    redirect: "/customer/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/customer/index"),
        meta: { title: "顾客模块管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/customer/edit"),
        hidden: true,
        meta: { title: "修改顾客模块" }
    },
    {
        path: "add",
        component: () => import("@/views/customer/add"),
        hidden: true,
        meta: { title: "添加顾客模块" }
    }
    ]
}

export default customerRouter
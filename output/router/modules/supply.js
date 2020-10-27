import Layout from "@/layout"

const supplyRouter = {
    path: "/supply",
    name: "supply",
    redirect: "/supply/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/supply/index"),
        meta: { title: "货源管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/supply/edit"),
        hidden: true,
        meta: { title: "修改货源" }
    },
    {
        path: "add",
        component: () => import("@/views/supply/add"),
        hidden: true,
        meta: { title: "添加货源" }
    }
    ]
}

export default supplyRouter
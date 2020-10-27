import Layout from "@/layout"

const brandRouter = {
    path: "/brand",
    name: "brand",
    redirect: "/brand/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/brand/index"),
        meta: { title: "品牌管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/brand/edit"),
        hidden: true,
        meta: { title: "修改品牌" }
    },
    {
        path: "add",
        component: () => import("@/views/brand/add"),
        hidden: true,
        meta: { title: "添加品牌" }
    }
    ]
}

export default brandRouter
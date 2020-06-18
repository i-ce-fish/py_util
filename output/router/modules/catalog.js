import Layout from "@/layout"

const catalogRouter = {
    path: "/catalog",
    name: "catalog",
    redirect: "/catalog/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/catalog/index"),
        meta: { title: "图文分类管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/catalog/edit"),
        hidden: true,
        meta: { title: "修改图文分类" }
    },
    {
        path: "add",
        component: () => import("@/views/catalog/add"),
        hidden: true,
        meta: { title: "添加图文分类" }
    }
    ]
}

export default catalogRouter
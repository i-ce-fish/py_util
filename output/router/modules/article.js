import Layout from "@/layout"

const articleRouter = {
    path: "/article",
    name: "article",
    redirect: "/article/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/article/index"),
        meta: { title: "图文模块管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/article/edit"),
        hidden: true,
        meta: { title: "修改图文模块" }
    },
    {
        path: "add",
        component: () => import("@/views/article/add"),
        hidden: true,
        meta: { title: "添加图文模块" }
    }
    ]
}

export default articleRouter
import Layout from "@/layout"

const categoryRouter = {
    path: "/category",
    name: "category",
    redirect: "/category/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/category/index"),
        meta: { title: "商品分类管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/category/edit"),
        hidden: true,
        meta: { title: "修改商品分类" }
    },
    {
        path: "add",
        component: () => import("@/views/category/add"),
        hidden: true,
        meta: { title: "添加商品分类" }
    }
    ]
}

export default categoryRouter
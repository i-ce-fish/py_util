import Layout from "@/layout"

const goodpatternRouter = {
    path: "/goodpattern",
    name: "goodpattern",
    redirect: "/goodpattern/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/goodpattern/index"),
        meta: { title: "商品图案管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodpattern/edit"),
        hidden: true,
        meta: { title: "修改商品图案" }
    },
    {
        path: "add",
        component: () => import("@/views/goodpattern/add"),
        hidden: true,
        meta: { title: "添加商品图案" }
    }
    ]
}

export default goodpatternRouter
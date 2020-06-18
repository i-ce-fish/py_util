import Layout from "@/layout"

const {{ModelNameSingular}}Router = {
    path: "/{{ModelNameSingular}}",
    name: "{{ModelNameSingular}}",
    redirect: "/{{ModelNameSingular}}/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/{{ModelNameSingular}}/index"),
        meta: { title: "{{ModuleNameCn}}管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/{{ModelNameSingular}}/edit"),
        hidden: true,
        meta: { title: "修改{{ModuleNameCn}}" }
    },
    {
        path: "add",
        component: () => import("@/views/{{ModelNameSingular}}/add"),
        hidden: true,
        meta: { title: "添加{{ModuleNameCn}}" }
    }
    ]
}

export default {{ModelNameSingular}}Router

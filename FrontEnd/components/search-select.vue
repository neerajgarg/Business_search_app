<template>
  <div
    class="ui fluid search selection dropdown"
    :class="{ 'active visible':showMenu, 'error': isError, 'disabled': isDisabled }"
    @click="openOptions"
    @focus="openOptions"
  >
    <i class="dropdown icon"></i>
    <input
      class="search"
      autocomplete="off"
      tabindex="0"
      :id="id"
      :name="name"
      :value="searchText"
      @input="searchText = $event.target.value"
      ref="input"
      @focus.prevent="openOptions"
      @keyup.esc="closeOptions"
      @blur="blurInput"
      @keydown.up="prevItem"
      @keydown.down="nextItem"
      @keydown.enter.prevent=""
      @keyup.enter.prevent="enterItem"
      @keydown.delete="deleteTextOrItem"
    />
    <div
      class="text"
      :class="textClass" :data-vss-custom-attr="searchTextCustomAttr"
    >{{inputText}}
    </div>
    <div
      class="menu"
      ref="menu"
      @mousedown.prevent
      :class="menuClass"
      :style="menuStyle"
      tabindex="-1"
    >
      <div
        v-for="(option, idx) in filteredOptions"
        :key="idx"
        class="item"
        :class="{ 'selected': option.selected || pointer === idx }"
        :data-vss-custom-attr="customAttrs[idx] ? customAttrs[idx] : ''"
        @click.stop="selectItem(option)"
        @mousedown="mousedownItem"
        @mouseenter="pointerSet(idx)"
      >
        {{option.text}}
      </div>
    </div>
  </div>
</template>
